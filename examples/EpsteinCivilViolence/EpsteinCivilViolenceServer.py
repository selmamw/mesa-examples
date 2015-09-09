from EpsteinCivilViolence import Citizen, Cop, CivilViolenceModel
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid

COP_COLOR = "#000000"
AGENT_QUIET_COLOR = "#0066CC"
AGENT_REBEL_COLOR = "#CC0000"
JAIL_COLOR = "#757575"


def citizen_cop_portrayal(agent):
    if agent is None:
        return

    portrayal = {"Shape": "circle",
                 "x": agent.pos[0], "y": agent.pos[1],
                 "Filled": "true"}

    if type(agent) is Citizen:
        color = AGENT_QUIET_COLOR if agent.condition == "Quiescent" else \
            AGENT_REBEL_COLOR
        color = JAIL_COLOR if agent.jail_sentence else color
        portrayal["Color"] = color
        portrayal["r"] = 0.8
        portrayal["Layer"] = 0

    elif type(agent) is Cop:
        portrayal["Color"] = COP_COLOR
        portrayal["r"] = 0.5
        portrayal["Layer"] = 1
    return portrayal

canvas_element = CanvasGrid(citizen_cop_portrayal, 40, 40, 500, 500)
server = ModularServer(CivilViolenceModel, [canvas_element],
                      "Epstein Civil Violence",
                      height=40,
                      width=40,
                      citizen_density=.7,
                      cop_density=.074,
                      citizen_vision=7,
                      cop_vision=7,
                      legitimacy=.8,
                      max_jail_term=1000)
server.launch()
