function graph_dependencies -d 'Use graphviz to build a dependency graph of your js project'
  depcruise --exclude "^node_modules" --output-type dot src | dot -T svg > dependencygraph.svg
end
