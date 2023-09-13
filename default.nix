{ pkgs ? import <nixpkgs> {} }:

with pkgs;



let



in mkShell {

  packages = [
    (pkgs.python3.withPackages (ps: [
      ps.numpy
      ps.pandas
      ps.requests
    ]))

  ];
  buildInputs = [

    nodejs_20
    yarn

  ];

}
