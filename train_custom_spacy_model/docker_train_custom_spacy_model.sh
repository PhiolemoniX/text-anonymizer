#!/bin/sh
if [ ! -d "/app/custom_spacy_model/fi_datahel_spacy-0.0.2" ]; then
    echo "Custom spacy model not found, training..."
    python ./train_custom_spacy_model.py
  cp template_meta.json ../custom_spacy_model/fi_datahel_spacy-0.0.2/meta.json
  cp template_config.cfg ../custom_spacy_model/fi_datahel_spacy-0.0.2/config.cfg
fi


