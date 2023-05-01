module.exports = {
    name: "Mockoon",
    script: "mockoon-cli",
    args: "start --daemon-off --disable-log-to-file --data /runtime_data/lazy-lab.mockoon.json --port 3000",
    watch: ["/runtime_data",],
    // Specify delay between watch interval
    watch_delay: 30000
}

