SCRIPTS_FOLDER_PATH=$( dirname -- "$0"; )


. "${SCRIPTS_FOLDER_PATH}/common.sh"


MESSAGE="${1}"


is_running=$(is_service_running "${API_SERVICE_NAME}")

if [ "${is_running}" -eq "1" ]; then
  echo "Please start the '${API_SERVICE_NAME}' service!"
  exit 1
fi


echo "Generating migrations..."
docker compose exec "${API_SERVICE_NAME}" bash -c "alembic revision --autogenerate -m '${MESSAGE}'"
echo "Done!"
