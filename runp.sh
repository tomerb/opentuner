#!/bin/bash

# Define the test limits, dimensions, and domain
test_limits=(10 100 1000)
dimensions_list=(2 3 4 5 6 7 8 9 10)
domain_list=(5 10 100 250 500 750 1000 1500)

# Function to run the Python script
run_python_script() {
    local limit=$1
    local dimensions=$2
    local domain=$3
    python examples/rosenbrock/rosenbrock.py --test-limit "$limit" --dimensions "$dimensions" --domain "$domain" --metric-log "metric-data.csv"
}

export -f run_python_script

# Run in parallel
parallel -j 4 --progress run_python_script ::: "${test_limits[@]}" ::: "${dimensions_list[@]}" ::: "${domain_list[@]}"
