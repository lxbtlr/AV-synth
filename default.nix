{ pkgs ? import <nixpkgs> {} }:

with pkgs;



let



in mkShell {

  packages = [
    (pkgs.python311.withPackages (ps: [
      ps.selenium
      ps.rich
      ps.evdev
      ps.pynput
      ps.numpy
      ps.pandas
      ps.requests
    ]))
    geckodriver
  ];
  buildInputs = [

    nodejs_20
    yarn

  ];

}
