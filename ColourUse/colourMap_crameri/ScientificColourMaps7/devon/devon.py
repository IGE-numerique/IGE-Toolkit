# 
#         devon
#                   www.fabiocrameri.ch/colourmaps
from matplotlib.colors import LinearSegmentedColormap      
      
cm_data = [[0.17103, 0.1004, 0.29978],      
           [0.17087, 0.10414, 0.30337],      
           [0.17068, 0.10786, 0.30699],      
           [0.17046, 0.11159, 0.31061],      
           [0.17023, 0.11524, 0.31422],      
           [0.16997, 0.11894, 0.31784],      
           [0.1697, 0.12254, 0.32146],      
           [0.1694, 0.12624, 0.32509],      
           [0.16908, 0.12989, 0.32874],      
           [0.16874, 0.1335, 0.33238],      
           [0.16837, 0.13713, 0.33601],      
           [0.16801, 0.14077, 0.33967],      
           [0.16765, 0.14438, 0.34332],      
           [0.16728, 0.14799, 0.34698],      
           [0.16689, 0.1516, 0.35064],      
           [0.16648, 0.15524, 0.35429],      
           [0.16605, 0.15887, 0.35797],      
           [0.16562, 0.16251, 0.36164],      
           [0.1652, 0.16612, 0.36531],      
           [0.1648, 0.16979, 0.369],      
           [0.16439, 0.17341, 0.37268],      
           [0.16397, 0.17708, 0.37639],      
           [0.16353, 0.18072, 0.38008],      
           [0.16308, 0.1844, 0.3838],      
           [0.16264, 0.1881, 0.3875],      
           [0.1622, 0.19175, 0.39124],      
           [0.16176, 0.19545, 0.39496],      
           [0.16131, 0.19914, 0.3987],      
           [0.16084, 0.20287, 0.40244],      
           [0.16036, 0.20662, 0.40621],      
           [0.15991, 0.21033, 0.40998],      
           [0.15947, 0.21408, 0.41376],      
           [0.15904, 0.21784, 0.41755],      
           [0.1586, 0.2216, 0.42135],      
           [0.15814, 0.22538, 0.42518],      
           [0.15768, 0.22918, 0.42901],      
           [0.15723, 0.23298, 0.43287],      
           [0.15681, 0.23683, 0.43674],      
           [0.15639, 0.24063, 0.44063],      
           [0.15595, 0.24449, 0.44456],      
           [0.15552, 0.24839, 0.44851],      
           [0.1551, 0.25226, 0.45249],      
           [0.15469, 0.25615, 0.45649],      
           [0.15431, 0.26008, 0.46054],      
           [0.15394, 0.26403, 0.46464],      
           [0.1536, 0.26797, 0.46878],      
           [0.15329, 0.27194, 0.47296],      
           [0.153, 0.27597, 0.47721],      
           [0.15276, 0.27998, 0.48152],      
           [0.15256, 0.28401, 0.48589],      
           [0.15241, 0.28806, 0.49034],      
           [0.15232, 0.29214, 0.49486],      
           [0.1523, 0.29622, 0.49944],      
           [0.15234, 0.30031, 0.50414],      
           [0.15246, 0.30441, 0.5089],      
           [0.15267, 0.30853, 0.51375],      
           [0.15298, 0.31262, 0.51869],      
           [0.15339, 0.31673, 0.52371],      
           [0.15391, 0.32082, 0.52882],      
           [0.15456, 0.32486, 0.53399],      
           [0.15532, 0.32892, 0.53926],      
           [0.15623, 0.33293, 0.5446],      
           [0.15721, 0.33688, 0.55],      
           [0.15838, 0.3408, 0.55545],      
           [0.15962, 0.34465, 0.56096],      
           [0.16105, 0.34846, 0.56651],      
           [0.16259, 0.3522, 0.57209],      
           [0.16426, 0.35588, 0.57769],      
           [0.166, 0.35947, 0.58331],      
           [0.1679, 0.36299, 0.58894],      
           [0.16993, 0.36646, 0.59458],      
           [0.17202, 0.36982, 0.60021],      
           [0.17425, 0.37313, 0.60583],      
           [0.17653, 0.37638, 0.61145],      
           [0.17895, 0.37954, 0.61705],      
           [0.1814, 0.38265, 0.62262],      
           [0.18398, 0.3857, 0.62819],      
           [0.18662, 0.38871, 0.63374],      
           [0.18934, 0.39167, 0.63926],      
           [0.19213, 0.39459, 0.64477],      
           [0.19503, 0.39748, 0.65028],      
           [0.19798, 0.40036, 0.65577],      
           [0.20103, 0.40321, 0.66124],      
           [0.20423, 0.40606, 0.66671],      
           [0.20748, 0.40891, 0.67218],      
           [0.21086, 0.41176, 0.67765],      
           [0.21438, 0.41463, 0.68311],      
           [0.21803, 0.41753, 0.68857],      
           [0.22183, 0.42044, 0.69402],      
           [0.22582, 0.42338, 0.69948],      
           [0.22993, 0.42637, 0.70494],      
           [0.23429, 0.42941, 0.71039],      
           [0.23881, 0.43249, 0.71584],      
           [0.24355, 0.43562, 0.72126],      
           [0.24855, 0.43878, 0.72667],      
           [0.25373, 0.44203, 0.73207],      
           [0.25915, 0.4453, 0.73742],      
           [0.26478, 0.44865, 0.74275],      
           [0.27068, 0.45204, 0.74803],      
           [0.27677, 0.45548, 0.75325],      
           [0.28309, 0.45897, 0.75842],      
           [0.28962, 0.4625, 0.76352],      
           [0.29635, 0.46607, 0.76854],      
           [0.30326, 0.46969, 0.77347],      
           [0.31037, 0.47331, 0.77832],      
           [0.3176, 0.47697, 0.78307],      
           [0.32497, 0.48065, 0.78772],      
           [0.33249, 0.48433, 0.79227],      
           [0.34009, 0.48804, 0.7967],      
           [0.34779, 0.49174, 0.80103],      
           [0.35555, 0.49542, 0.80525],      
           [0.36336, 0.49911, 0.80936],      
           [0.37122, 0.50278, 0.81336],      
           [0.37911, 0.50644, 0.81727],      
           [0.38701, 0.51008, 0.82107],      
           [0.39494, 0.51371, 0.82478],      
           [0.40285, 0.51731, 0.8284],      
           [0.41076, 0.52088, 0.83194],      
           [0.41863, 0.52444, 0.8354],      
           [0.4265, 0.52797, 0.83878],      
           [0.43435, 0.53148, 0.84211],      
           [0.44217, 0.53496, 0.84536],      
           [0.44995, 0.53844, 0.84856],      
           [0.45769, 0.54187, 0.85171],      
           [0.46541, 0.54531, 0.85481],      
           [0.47308, 0.54872, 0.85786],      
           [0.48073, 0.55212, 0.86088],      
           [0.48834, 0.55549, 0.86386],      
           [0.49589, 0.55887, 0.8668],      
           [0.50341, 0.56225, 0.8697],      
           [0.51089, 0.5656, 0.87258],      
           [0.51834, 0.56896, 0.87542],      
           [0.52572, 0.57232, 0.87823],      
           [0.53305, 0.57568, 0.88101],      
           [0.54033, 0.57904, 0.88375],      
           [0.54755, 0.58241, 0.88646],      
           [0.55471, 0.58579, 0.88913],      
           [0.5618, 0.58917, 0.89176],      
           [0.56881, 0.59258, 0.89435],      
           [0.57576, 0.59599, 0.89689],      
           [0.5826, 0.59942, 0.89939],      
           [0.58935, 0.60286, 0.90183],      
           [0.59601, 0.60632, 0.90422],      
           [0.60256, 0.6098, 0.90655],      
           [0.60899, 0.61329, 0.90881],      
           [0.61529, 0.6168, 0.91102],      
           [0.62146, 0.62032, 0.91315],      
           [0.62749, 0.62385, 0.91521],      
           [0.63338, 0.62739, 0.9172],      
           [0.63911, 0.63094, 0.9191],      
           [0.64469, 0.63449, 0.92093],      
           [0.65011, 0.63804, 0.92269],      
           [0.65537, 0.64159, 0.92436],      
           [0.66048, 0.64514, 0.92595],      
           [0.66542, 0.6487, 0.92746],      
           [0.67022, 0.65223, 0.9289],      
           [0.67484, 0.65577, 0.93027],      
           [0.67933, 0.65928, 0.93157],      
           [0.68368, 0.66279, 0.93279],      
           [0.68789, 0.66628, 0.93396],      
           [0.69197, 0.66977, 0.93506],      
           [0.69594, 0.67324, 0.93611],      
           [0.69978, 0.67669, 0.93711],      
           [0.70354, 0.68012, 0.93806],      
           [0.7072, 0.68355, 0.93896],      
           [0.71077, 0.68697, 0.93983],      
           [0.71427, 0.69038, 0.94067],      
           [0.71771, 0.69377, 0.94147],      
           [0.72108, 0.69716, 0.94225],      
           [0.72441, 0.70054, 0.943],      
           [0.72769, 0.70392, 0.94373],      
           [0.73094, 0.70728, 0.94445],      
           [0.73416, 0.71065, 0.94515],      
           [0.73734, 0.71401, 0.94583],      
           [0.74051, 0.71738, 0.94651],      
           [0.74366, 0.72073, 0.94718],      
           [0.7468, 0.72408, 0.94784],      
           [0.74992, 0.72744, 0.9485],      
           [0.75303, 0.7308, 0.94915],      
           [0.75615, 0.73416, 0.9498],      
           [0.75925, 0.73752, 0.95045],      
           [0.76236, 0.74089, 0.9511],      
           [0.76546, 0.74426, 0.95174],      
           [0.76856, 0.74763, 0.95238],      
           [0.77167, 0.75101, 0.95302],      
           [0.77477, 0.75438, 0.95367],      
           [0.77788, 0.75776, 0.95431],      
           [0.78098, 0.76114, 0.95495],      
           [0.7841, 0.76453, 0.95559],      
           [0.78721, 0.76791, 0.95623],      
           [0.79032, 0.77131, 0.95687],      
           [0.79344, 0.7747, 0.95752],      
           [0.79656, 0.77811, 0.95816],      
           [0.79969, 0.78151, 0.95881],      
           [0.80281, 0.78492, 0.95945],      
           [0.80595, 0.78833, 0.9601],      
           [0.80909, 0.79175, 0.96074],      
           [0.81222, 0.79517, 0.96139],      
           [0.81537, 0.79859, 0.96203],      
           [0.81851, 0.80202, 0.96269],      
           [0.82167, 0.80545, 0.96334],      
           [0.82482, 0.80889, 0.96398],      
           [0.82797, 0.81233, 0.96463],      
           [0.83114, 0.81577, 0.96529],      
           [0.8343, 0.81921, 0.96594],      
           [0.83747, 0.82267, 0.96659],      
           [0.84064, 0.82612, 0.96725],      
           [0.84381, 0.82958, 0.9679],      
           [0.84699, 0.83304, 0.96856],      
           [0.85017, 0.83651, 0.96921],      
           [0.85336, 0.83998, 0.96987],      
           [0.85655, 0.84345, 0.97053],      
           [0.85974, 0.84693, 0.97118],      
           [0.86294, 0.85041, 0.97184],      
           [0.86614, 0.85389, 0.97251],      
           [0.86934, 0.85739, 0.97316],      
           [0.87255, 0.86088, 0.97382],      
           [0.87576, 0.86438, 0.97448],      
           [0.87897, 0.86788, 0.97515],      
           [0.88219, 0.87138, 0.97581],      
           [0.88541, 0.87489, 0.97647],      
           [0.88864, 0.8784, 0.97714],      
           [0.89186, 0.88192, 0.9778],      
           [0.8951, 0.88544, 0.97847],      
           [0.89833, 0.88896, 0.97914],      
           [0.90157, 0.89249, 0.97981],      
           [0.90481, 0.89602, 0.98047],      
           [0.90806, 0.89956, 0.98114],      
           [0.9113, 0.9031, 0.98181],      
           [0.91456, 0.90664, 0.98248],      
           [0.91781, 0.91019, 0.98315],      
           [0.92107, 0.91374, 0.98382],      
           [0.92433, 0.91729, 0.9845],      
           [0.92759, 0.92084, 0.98517],      
           [0.93087, 0.92441, 0.98584],      
           [0.93413, 0.92797, 0.98652],      
           [0.93741, 0.93154, 0.98719],      
           [0.94069, 0.93511, 0.98786],      
           [0.94397, 0.93869, 0.98854],      
           [0.94725, 0.94227, 0.98921],      
           [0.95053, 0.94585, 0.98989],      
           [0.95382, 0.94944, 0.99056],      
           [0.95711, 0.95303, 0.99124],      
           [0.9604, 0.95662, 0.99191],      
           [0.96369, 0.96022, 0.99259],      
           [0.96698, 0.96382, 0.99326],      
           [0.97027, 0.96742, 0.99393],      
           [0.97357, 0.97102, 0.9946],      
           [0.97686, 0.97463, 0.99527],      
           [0.98016, 0.97824, 0.99594],      
           [0.98345, 0.98186, 0.99662],      
           [0.98675, 0.98548, 0.99728],      
           [0.99004, 0.9891, 0.99795],      
           [0.99334, 0.99272, 0.99862],      
           [0.99662, 0.99634, 0.99929],      
           [0.99992, 0.99997, 0.99995]]      
      
devon_map = LinearSegmentedColormap.from_list('devon', cm_data)      
# For use of "viscm view"      
test_cm = devon_map      
      
if __name__ == "__main__":      
    import matplotlib.pyplot as plt      
    import numpy as np      
      
    try:      
        from viscm import viscm      
        viscm(devon_map)      
    except ImportError:      
        print("viscm not found, falling back on simple display")      
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',      
                   cmap=devon_map)      
    plt.show()      
