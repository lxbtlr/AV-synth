{ pkgs ? import <nixpkgs> {} }:

with pkgs;



let



in mkShell {

  packages = [
    (pkgs.python311.withPackages (ps: [
      ps.selenium
      ps.keyboard
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
