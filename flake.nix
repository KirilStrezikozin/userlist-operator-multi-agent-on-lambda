{
  description = "Nix flake for local development";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";

    systems.url = "github:nix-systems/default-linux";
  };

  outputs =
    {
      nixpkgs,
      systems,
      ...
    }:
    let
      inherit (nixpkgs) lib;
      eachSystem = lib.genAttrs (import systems);

      pkgsFor = eachSystem (
        system:
        import nixpkgs {
          localSystem = system;
          config = {
            allowUnfree = true;
          };
        }
      );

    in
    {
      devShells = eachSystem (system: rec {
        default = develop;

        develop = pkgsFor.${system}.mkShell {
          packages = with pkgsFor.${system}; [
            uv
            ruff
            terraform
            terraform-providers.aws
            awscli2

            pyright
            nixd
            terraform-lsp
          ];

          shellHook = ''
          uv sync
          source ./.venv/bin/activate
          '';
        };
      });

      formatter = eachSystem (system: pkgsFor.${system}.nixfmt);
    };
}
