#!/bin/sh
VERSION=$(python /app/get_model_version.py)
if [ ! -d "/app/custom_spacy_model/fi_datahel_spacy-${VERSION}" ]; then
    echo "Custom spacy model not found, training..."
    python ./train_custom_spacy_model.py
    cp template_meta_spacy_fi_lg.json ../custom_spacy_model/fi_datahel_spacy-${VERSION}/meta.json
    cp template_config_spacy_fi_lg.cfg ../custom_spacy_model/fi_datahel_spacy-${VERSION}/config.cfg
fi


