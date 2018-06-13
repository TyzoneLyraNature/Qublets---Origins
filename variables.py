# WINDOW / GAME_AREA
## Modifié pour commencer avec WINDOW_, GAME_AREA_
# ATTENTION : Ces variables sont également définies dans projetMajeure.py.
# Pensez à les modifier là-bas aussi ou à faire une variable partagée

clearCommand = "cls"

WINDOW_WIDTH = 1000 #800
WINDOW_HEIGHT = 800 #500

GAME_AREA_WIDTH = 800 #500
GAME_AREA_HEIGHT = 800 #500

# AGENT
## Modifié pour commencer avec AGENT_
AGENT_PV_INITIAL = 3
AGENT_WIDTH = 16 #32
AGENT_HEIGHT = 16 #32
AGENT_VITESSE = 4 #10
NB_AGENTS_BLEUS = 20
NB_AGENTS_ROUGES = 20
#AGENT_DR = np.pi/30
AGENT_DR = 5 #en degrés

# PROJECTILE
## Modifié pour commencer avec PROJECTILE_
PROJECTILE_DAMAGE = 1
PROJECTILE_WIDTH = 4 #8
PROJECTILE_HEIGHT = 4 #8
PROJECTILE_VITESSE = 8 #20

# RESSOURCE
## Pas modifié, juste organisé
RESOURCE_WIDTH = 12 #24
RESOURCE_HEIGHT = 12 #24
RESOURCE_REWARD = 400
NB_MAX_RESOURCES = 20

global startTime
startTime = 0


# TEAM
## Modifié pour commencer avec TEAM_
TEAM_BLUE = 1
TEAM_RED = 2

# IMAGEPATHS
IMAGEPATH_404 = "Images/ImageNotFound_32.png"
IMAGEPATH_AGENT_BLEU = "Images/AgentBleu_32.png"
IMAGEPATH_AGENT_ROUGE = "Images/AgentRouge_32.png"
IMAGEPATH_AGENT_NEUTRE = "Images/AgentNeutre_32.png"
IMAGEPATH_RESOURCE = "Images/Resource_24.png"
IMAGEPATH_PROJECTILE_BLEU = "Images/Projectile_Bleu_8.png"
IMAGEPATH_PROJECTILE_ROUGE = "Images/Projectile_Rouge_8.png"

IMAGEPATH_404 = "Images/ImageNotFound.png"
IMAGEPATH_AGENT_BLEU = "Images/AgentBleu.png"
IMAGEPATH_AGENT_ROUGE = "Images/AgentRouge.png"
IMAGEPATH_AGENT_NEUTRE = "Images/AgentNeutre.png"
IMAGEPATH_RESOURCE = "Images/Resource.png"
IMAGEPATH_PROJECTILE_BLEU = "Images/Projectile_Bleu.png"
IMAGEPATH_PROJECTILE_ROUGE = "Images/Projectile_Rouge.png"

#Action possible
## Modifié pour commencer avec ACTION_

ACTION_STOP = 5
ACTION_MOVE = 0
ACTION_TRIGO = 1
ACTION_HORAIRE = 2
ACTION_SHOOT = 3
ACTION_BUILD = 8008135
ACTIONS = [ACTION_MOVE,ACTION_TRIGO,ACTION_HORAIRE, ACTION_SHOOT]



#TYPE
## Modifié pour commencer avec TYPE
TYPE_RESOURCE = 0
TYPE_AGENT = 1
TYPE_PROJECTILE = 2
TYPE_BLOCK = 3

#TRAINING
## Modifié pour commencer avec TRAINING_
TRAINING_N_EPISODE = 200
TRAINING_N_STEP = 1000
TRAINING_GAMMA = 0.98
TRAINING_LEARNING_RATE = 0.01

#N_STATE = len([0:np.sqrt(H*H+W*W):])
global q_table_E1, q_table_E2
q_table_E1 = {} #equipe bleu
q_table_E2 = {} #equipe rouge
eps = 0.05

global total_reward_bleu, total_reward_rouge
total_reward_bleu = []
total_reward_rouge = []