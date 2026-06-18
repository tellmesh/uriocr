from __future__ import annotations

from urisysedge.runtime import Runtime

from uriocr import register as register_ocr


def test_latest_text_mock():
    rt = Runtime(config={"ocr": {"driver": "mock"}})
    register_ocr(rt)
    res = rt.call("ocr://local/image/latest/query/text", {}, {})
    assert res["ok"]
    assert "OK" in res["result"]["text"]


def test_image_text_mock():
    rt = Runtime(config={"ocr": {"driver": "mock"}})
    register_ocr(rt)
    res = rt.call("ocr://local/image/shot-1/query/text", {}, {"params": {"image_id": "shot-1"}})
    assert res["ok"]
    assert res["result"]["image_id"] == "shot-1"


def test_image_text_reads_screenshot_registry():
    import base64

    rt = Runtime(config={"ocr": {"driver": "mock"}})
    register_ocr(rt)
    image_id = "shot-registry"
    rt.state["images"] = {
        image_id: {
            "image_id": image_id,
            "mime": "text/plain",
            "base64": base64.b64encode(b"Install OK Cancel").decode("ascii"),
        }
    }
    res = rt.call(
        f"ocr://local/image/{image_id}/query/text",
        {},
        {"params": {"image_id": image_id}},
    )
    assert res["ok"]
    assert res["result"]["image_id"] == image_id
