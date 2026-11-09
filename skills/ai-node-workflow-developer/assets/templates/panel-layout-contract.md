# Panel Layout Contract

- Screen ID:
- Approved prototype version / date:
- Primary user task:
- Minimum supported app/window size:
- Layout modes + breakpoint reasoning (preferred widths based on content, not device labels):

| Panel ID | Role | Preferred W/H | Min W/H | Max W/H | Resize | Priority | On narrow/short viewport | Overflow/scroll | State persistence |
|---|---|---|---|---|---|---|---|---|---|
| PAN-PREVIEW | Main preview | | | | fit container | High | focus panel / full width | contain content | |
| PAN-TOOLS | Tools | | | | none | High | icon row + overflow menu | independent scroll | |
| PAN-INSPECTOR | Properties | | | | splitter | Medium | drawer/tab | vertical scroll | clamp persisted width |

## Preview-specific zoom
- Asset/media kind + aspect ratio:
- Preview container resize behavior:
- Initial display scale / fit-to-view:
- Min/max zoom, step and smooth animation:
- Mouse/trackpad/touch/keyboard interactions:
- Zoom focal point and pan constraints:
- Reset/fit behavior:
- Does zoom affect exports? (usually NO):

## Toolbar and help behavior
- Button IDs preserved across layout modes:
- Button priority + collapse order:
- Overflow menu IDs and where hidden commands move:
- Contextual `?` help popup placement and dismissal:
- Essential labels and warnings never hidden:

## Acceptance
- Expected screenshots by mode:
- Layout test matrix file:
- Known layout exceptions:
- Product owner approval / change request:
