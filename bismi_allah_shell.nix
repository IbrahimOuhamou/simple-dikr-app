#بسم الله الرحمن الرحيم
let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.kivy
      python-pkgs.python-bidi
      python-pkgs.arabic-reshaper
    ]))
  ];
}
