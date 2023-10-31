function create-docker-diagram
  podman run --rm -it --name dcv -v $(pwd):/input docker.io/pmsipilot/docker-compose-viz render --no-volumes --force -o $argv.png -m image $argv;
end
