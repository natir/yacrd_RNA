
configfile: "etc/config.yaml"

include: "rules/data.snk"
include: "rules/simulate.snk"
include: "rules/detect.snk"

rule all:
    input:
        rules.data.input,
        rules.simulate.input,
        rules.detect.input,
