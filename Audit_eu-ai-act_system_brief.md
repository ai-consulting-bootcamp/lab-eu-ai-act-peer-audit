## System brief

| Kick-off question | Answer |
|---|---|
| **What does the system do?** | Green Warehouse Network helps a logistics planner choose warehouses in Germany. It gives each customer a main warehouse and a second warehouse to use if the first is unavailable. The planner can ask “what if” questions, such as closing a warehouse, increasing demand, using electric trucks, or choosing lower cost instead of lower emissions. |
| **What inputs does it take?** | It reads customer and warehouse information from local data files. Customer records contain an ID, business or city name, location, and yearly demand. Warehouse records contain an ID, location, capacity, yearly fixed cost, and yearly emissions. It also uses emissions estimates from Climatiq and cached road distances prepared with OpenRouteService. The sample data has no names, contact details, or other direct personal data. Personal data is not needed and should not be entered into the chat. |
| **What does it output?** | It produces a planning recommendation, not an order or automatic action. The output lists warehouses to open, each customer’s main and backup warehouse, yearly cost, yearly CO₂ emissions, average distances, warnings, and the effect of a warehouse failure. It can compare different situations and create a downloadable report. It does not send emails, change warehouse operations, or contact customers. |
| **Who is affected?** | The direct users are logistics and supply-chain planners at the client organisation. The results may affect future warehouse and transport planning, but customers, warehouse workers, and members of the public do not use the system directly and are not automatically assessed by it. |
| **Does a human review the output?** | Yes. Before using a result, a logistics or network-planning professional checks the input data and chosen goal, reads warnings and the calculation status, reviews each customer’s main and backup warehouse, and tests important failures or alternative assumptions. They decide whether the recommendation is suitable for a real planning meeting. The application has no automatic approval or execution step. |
| **Who built it?** | Our project team built this course project. We configured third-party services for language understanding, emissions data, and road-distance data. The warehouse calculations and validation rules are part of this project. |
| **Who would use it in production?** | The client’s supply-chain or logistics-planning staff would use it for network-planning discussions and comparisons. It is not intended for customers, warehouse workers, applicants, or members of the public. |

## Technical documentation and architecture

The system has four main layers:

```text
User describes a planning question
              |
              v
Streamlit dashboard (chat, maps, results, report download)
              |
              v
Conversation helper (understands the request and asks for clarification)
              |
              v
Input checks and warehouse calculator
              |
              v
Warehouse choices, customer assignments, cost, CO₂, warnings
```

Local customer, warehouse, emissions, and distance files feed the input checks and warehouse calculator. The conversation helper uses an OpenAI language service to understand plain-English requests and explain results. It does not calculate warehouse choices or invent the figures. The calculator uses the project’s fixed rules and the PuLP/CBC solver to find a network with a main and backup warehouse for every customer. The dashboard displays the result and can create a report.

| Technical area | What it contains | File or location |
|---|---|---|
| User interface | Chat, objective choice, maps, key figures, failure view, scenario comparison, and report download | [`app.py`](app.py) |
| Conversation flow | Reads a user request, keeps the current situation, checks missing or invalid information, and explains the result | [`agent/graph.py`](agent/graph.py), [`agent/schema.py`](agent/schema.py) |
| Input checks and tools | Checks warehouse IDs, customer data, allowed ranges, capacity warnings, and scenario requests | [`src/tools.py`](src/tools.py), [`src/schema.py`](src/schema.py) |
| Warehouse calculation | Chooses open warehouses and main/backup assignments; calculates cost, CO₂, capacity, and failure results | [`src/model.py`](src/model.py) |
| Source data | 24 customers, 12 candidate warehouses, emissions values, and cached distance data | [`data/`](data/) |
| Tests | Checks calculation paths, error handling, and plain-English request handling | [`tests/`](tests/) |

### Audit-relevant boundaries

- The tool uses static planning data; it does not connect to live warehouse or customer systems.
- Every result includes a calculation status and warnings when the requested situation cannot be solved or needs attention.
- The language service can understand and explain requests, but the project calculator supplies the numbers.
- No result automatically changes operations or makes a decision about a person.
- The current design requires human review before a recommendation is used.

Further course documentation is available in the [full specification](docs/Spec.md), the [technology decision](docs/stack_decision.md), and the [README](README.md).
