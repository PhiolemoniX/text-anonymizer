@echo off
FOR /F %%i IN ('python ..\get_model_version.py') DO SET VERSION=%%i
python train_custom_spacy_model.py
copy template_meta_spacy_fi_lg.json ..\custom_spacy_model\fi_datahel_spacy-%VERSION%\meta.json
copy template_config_spacy_fi_lg.cfg ..\custom_spacy_model\fi_datahel_spacy-%VERSION%\config.cfg
cd ..
pip install -e custom_spacy_model
cd train_custom_spacy_model
python evaluation.py
