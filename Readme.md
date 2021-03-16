# Yacrd RNA

Just a pipeline to try to evaluate [yacrd](https://github.com/natir/yacrd/) on RNA dataset.

You can launch pipeline:
```
cp etc/config.example.yaml etc/config.yaml
# edit etc/config.yaml

snakemake -r -p --use-conda
```

If you didn't want use conda you need to have in your path:
- [yacrd](https://github.com/natir/yacrd/)
- [Badread](https://github.com/rrwick/Badread)
- [minimap2](https://github.com/lh3/minimap2)

After run pipeline you can use jupyter notebook `notebook.ipynb` to compute some result.
