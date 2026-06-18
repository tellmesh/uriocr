from __future__ import annotations

from importlib.resources import as_file

from uri_control import CapabilityRegistry

import uriocr


def test_manifest_loads():
    with as_file(uriocr.manifest_path()) as path:
        registry = CapabilityRegistry.from_manifest_files([path])
    assert registry.manifests[0].scheme == "ocr"
    assert len(registry.routes) == 2


def test_manifest_matches_routes():
    from uri_control.edge.runtime import Runtime

    rt = Runtime(config={"ocr": {"driver": "mock"}})
    uriocr.register(rt)
    patterns = {route.pattern for route in rt.routes}
    assert patterns == {
        "ocr://{host}/image/latest/query/text",
        "ocr://{host}/image/{image_id}/query/text",
    }
