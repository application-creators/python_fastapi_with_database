

VIRTUALENV_PATH=./venv

REQUIREMENTS_FILE_PATH=./requirements.frozen
TEST_REQUIREMENTS_FILE_PATH=./requirements.test.frozen


create_virtualenv:
	@echo "Creating virtualenv..."
	python3 -m venv "${VIRTUALENV_PATH}"
	@echo "Done!"


install_requirements:
	@echo "Installing requirements..."
	${VIRTUALENV_PATH}/bin/pip install -r "${REQUIREMENTS_FILE_PATH}"
	@echo "Done!"


install_test_requirements:
	@echo "Installing test requirements..."
	${VIRTUALENV_PATH}/bin/pip install -r "${TEST_REQUIREMENTS_FILE_PATH}"
	@echo "Done!"


install_all_requirements: install_requirements install_test_requirements


run_unit_tests:
	@echo "Running unit tests..."
	@. ${VIRTUALENV_PATH}/bin/activate && \
	cd {{ cookiecutter.project_package_name }} && \
	python -m unittest discover -s . -p '*_test.py' && \
	cd ..
	@echo "Done!"


generate_database_migration:
	@./{{ cookiecutter.project_package_name }}/scripts/generate_database_migration.sh "${MESSAGE}"


migrate_database:
	@./{{ cookiecutter.project_package_name }}/scripts/migrate_database.sh
