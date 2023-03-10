#! /bin/bash
zip -r archive.zip * -x "*venv*"
eb deploy
