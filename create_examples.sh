# Calls all python programs to create example plots in examples/ directory

for i in ./examples/*.py; do
    python $i
done