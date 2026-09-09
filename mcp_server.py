"""MCP Server for Sutherland-Hodgman Polygon Clipping Skill."""
import json
import sys
from client import SutherlandHodgman

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "clip_polygon",
                            "description": "Clip subject polygon against a convex clipping window",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "subject_polygon": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    },
                                    "clip_polygon": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    }
                                },
                                "required": ["subject_polygon", "clip_polygon"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                subj = [tuple(p) for p in args["subject_polygon"]]
                clip_win = [tuple(p) for p in args["clip_polygon"]]
                result = SutherlandHodgman.clip(subj, clip_win)
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"clipped_polygon": result, "vertices": len(result)})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
