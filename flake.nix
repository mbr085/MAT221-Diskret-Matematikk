{
  description = "MAT221 Diskret matematikk";

  inputs.teaching.url = "github:mbr085/TeachingEnvironment";

  outputs = { teaching, ... }: {
    devShells = teaching.devShells;
  };
}
