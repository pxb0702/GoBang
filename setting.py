
# this class is to store all settings of the GoBang. 

class Settings_Environment() : 
	def __init__(self) : 
# define the UI window length and width, Length > Width, we need some display on the side
		self.screen_width = 1200
		self.screen_height = 800
# windows back ground color
		self.bg_color_Window = (200, 200, 200)
# Gobang play place color
		self.bg_color_Gobang_chess_board = (200,200,0) 
# Gobang line color
		self.Gobang_line_color = (0, 0, 0)
# Gobang black chess piece image 
		self.Gobang_chess_piece_black_image = ""		
# Gobang white chess piece image 
		self.Gobang_chess_piece_white_image = ""
# Gobang Chess board size  
		self.chess_board_size = 15
# Where to store Gobang training result  
		self.traing_check_point_directory = "./CKPT"  
		


# -------------------------------------------------------------------#
# Function name = intialize_settings 								 #
# Parameter :														 #
#	self : class object												 #
#	size : to set the size of the chess board, default is 15 x 15	 #
# return : None														 #	
#--------------------------------------------------------------------#
	def initialize_settings(self, size = 15) :
		self.chess_board_size = size
		
		
# -------------------------------------------------------------------#
# class name = Settings_CNN			 								 #
# Functions :														 #
#	init : initialize the parameters 								 #
#--------------------------------------------------------------------#

class Settings_CNN() : 
	def __init__(self, CNN_layers = 10, FC_nodes = 1024) : 
		self.CNN_layers = CNN_layers
		self.FC_nodes = FC_nodes








