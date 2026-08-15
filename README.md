# MAT221 Diskret matematikk

Quarto-baserte undervisningsnotater for MAT221.

## Arkitektur

Dette repositoryet inneholder selve kursmaterialet.

- **Quarto og LaTeX** kommer fra Home Manager (`home.nix`).
- **Python/Jupyter** kommer fra
  [`mbr085/TeachingEnvironment`](https://github.com/mbr085/TeachingEnvironment).
- **`.qmd` er kildeformatet**.
- Utvalgte `.qmd`-filer eksporteres til `.ipynb` for Google Colab.
- Quarto bygger HTML-boken til `docs/`.

## Første gangs oppsett

```bash
git init
nix flake lock
direnv allow
```

Kontroller deretter:

```bash
which quarto
which python
echo "$QUARTO_PYTHON"

quarto --version
python --version
quarto check jupyter
```

`quarto` skal komme fra Home Manager, mens `python` skal komme fra
`TeachingEnvironment`.

## Daglig bruk

```bash
make preview
make html
make pdf
make colab
make check
```

## Legge til et nytt kapittel

Opprett for eksempel `notes/02-grafer.qmd` og legg filen til under
`book.chapters` i `_quarto.yml`.

Hvis kapitlet også skal kunne åpnes i Google Colab, legg samme filnavn til i
`colab-files.txt`.

## Oppdatere felles undervisningsmiljø

Hvert kurs har sin egen `flake.lock`. Når du vil oppdatere til nyeste versjon:

```bash
nix flake update teaching
make check
```

## GitHub Pages

HTML bygges til `docs/`.

Et enkelt første oppsett er å committe `docs/` og på GitHub velge:

**Settings → Pages → Deploy from a branch → main → /docs**
