.PHONY: preview render html pdf colab check clean

preview:
	quarto preview

render:
	quarto render

html:
	quarto render --to html

pdf:
	quarto render --to pdf

colab:
	./scripts/export-colab.sh

check:
	./scripts/check.sh

clean:
	rm -rf docs .quarto
