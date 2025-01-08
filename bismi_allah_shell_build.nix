#بسم الله الرحمن الرحيم
let
  pkgs = import <nixpkgs> {
    config = {
      allowUnfree = true;
      android_sdk.accept_license = true;
    };
  };
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.flet
    ]))
    pkgs.flutter
    pkgs.google-chrome
    pkgs.androidsdk
  ];

  shellHook = ''
    export CHROME_EXECUTABLE=`which google-chrome-stable`
  '';
}
