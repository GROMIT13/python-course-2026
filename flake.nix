{
  description = "Example python program";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    pkgs = nixpkgs.legacyPackages."x86_64-linux";
  in {
    devShells."x86_64-linux".default = pkgs.mkShell {
      packages = [
        (pkgs.python3.withPackages (pypkgs:
          with pypkgs; [
            numpy
          ]))

        #LSP
        pkgs.basedpyright
        #Formatter
        pkgs.ruff
        pkgs.black
      ];

      env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
        pkgs.stdenv.cc.cc.lib
        pkgs.libz
      ];

      shellHook = ''
        python --version
        exec fish
      '';
    };
  };
}
