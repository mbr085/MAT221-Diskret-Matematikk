.PHONY: preview render colab check clean

preview:
	quarto preview

render:
	quarto render

colab:
	./scripts/export-colab.sh

check:
	./scripts/check.sh

clean:
	rm -rf docs .quarto
