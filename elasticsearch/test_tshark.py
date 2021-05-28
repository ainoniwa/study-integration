from invoke import run


def test_tshark():
    run('curl -s -L -o dhcp.pcap "https://wiki.wireshark.org/SampleCaptures?action=AttachFile&do=get&target=dhcp.pcap"')
    run('tshark -r dhcp.pcap -T ek | jq -c "del(.index._type)" > dhcp.pcap.json')
    run('curl -s -H "Content-type: application/x-ndjson" -X POST ${ES}/_bulk -w "\n" --data-binary @dhcp.pcap.json')
    ret = run('curl -s -H "Content-type: application/json" ${ES}/_cat/indices')
    assert("packets-2004-12-06" in ret.stdout)
    run('curl -s -H "Content-type: application/json" -X DELETE -w "\n" ${ES}/packets-2004-12-06')
    ret = run('curl -s -H "Content-type: application/json" ${ES}/_cat/indices')
    assert("packets-2004-12-06" not in ret.stdout)
