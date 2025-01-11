#بسم الله الرحمن الرحيم
let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.flet
      python-pkgs.flet-desktop
    ]))
  ];
}
