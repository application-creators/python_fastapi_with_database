

API_SERVICE_NAME="{{ cookiecutter.project_package_name }}"


is_service_running() {
  service_name="${1}"

  if [ -z `docker compose ps -q ${service_name} 2>/dev/null` ] || [ -z `docker ps -q --no-trunc | grep $(docker compose ps -q ${service_name})` ]; then
    echo "1"
  else
    echo "0"
  fi
}
