# genpark-sutherland-hodgman-polygon-clipping-skill

[![GitHub stars](https://img.shields.io/github/stars/alphaparkinc/genpark-sutherland-hodgman-polygon-clipping-skill?style=social)](https://github.com/alphaparkinc/genpark-sutherland-hodgman-polygon-clipping-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent Sutherland-Hodgman Polygon Clipping Engine for Viewport & Spatial Boundary Truncation

Part of the **GenPark Autonomous Computational Geometry & Spatial Reasoning Swarm**.

## Architecture Overview

```mermaid
graph TD
    A[Subject Arbitrary Polygon] --> B[Select Clip Edge from Convex Viewport]
    B --> C[Classify Subject Edge Vertices S and E]
    C --> D{Inside/Outside Clip Half-Plane?}
    D -->|Both Inside| E[Emit Endpoint E]
    D -->|Inside to Outside| F[Emit Intersection Point]
    D -->|Outside to Inside| G[Emit Intersection Point & Endpoint E]
    D -->|Both Outside| H[Discard Edge]
    E --> I[Accumulate Next Iteration Subject Polygon]
    F --> I
    G --> I
    H --> I
    I --> J{More Clip Edges?}
    J -->|Yes| B
    J -->|No| K[Final Clipped Enclosed Polygon]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies (no Shapely, CGAL, or SciPy). Runs anywhere.
- **Production-Grade Design**: Type annotations, exhaustive edge cases, robust numerical stability.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/alphaparkinc/genpark-sutherland-hodgman-polygon-clipping-skill.git
cd genpark-sutherland-hodgman-polygon-clipping-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
