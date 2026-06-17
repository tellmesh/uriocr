from __future__ import annotations

from urisysedge.runtime import Runtime

import uriocr


def test_latest_text_mock():
    rt = Runtime(config={"ocr": {"driver": "mock"}})
    uriocr.register(rt)
    res = rt.call("ocr://local/image/latest/query/text", {}, {})
    assert res["ok"]
    assert "OK" in res["result"]["text"]


def test_image_text_mock():
    rt = Runtime(config={"ocr": {"driver": "mock"}})
    uriocr.register(rt)
    res = rt.call("ocr://local/image/shot-1/query/text", {}, {"params": {"image_id": "shot-1"}})
    assert res["ok"]
    assert res["result"]["image_id"] == "shot-1"
