function render-docker
  sudo docker run --rm -it --name dcv -v $(pwd):/input pmsipilot/docker-compose-viz render -f -r -m image docker-compose.yml
end
