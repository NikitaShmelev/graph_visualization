# you need numpy lib run next command in terminal " pip install -r libs.txt "
# python 3.8 + 
import numpy as np
import matplotlib.pyplot as plt


def read_file_and_get_array(file_name, array):
    file = open(file_name)
    data = file.readlines()
    file.close()
    for line in enumerate(data):
        row = list(
                    map(float, line[1].strip().split(';'))
                    )
        array.append(row)
    return array


def print_array(array):
    print(f'\nPrinting table: ')
    print('\t',('\t').join([str(i) for i in range(len(array))]))
    for line in array:
        print(f'\n{array.index(line)}\t', end='')
        for item in line:
            print(f'{item}\t', end='')
        
    print(f"Size {len(array)}x{len(array[0])}")

graph = read_file_and_get_array('Graph.csv', list())
coordinates = read_file_and_get_array('Coordinates.csv', list())
print_array(graph); print_array(coordinates)

fig, ax = plt.subplots()
x, y = [i[0] for i in coordinates], [i[1] for i in coordinates]
ax.plot(x, y, 'ro', markersize=23)

for i in enumerate(x):
    ax.annotate(str(i[0]),  xy=(i[1]+1, y[i[0]]+1), rotation=0)

legend_text = 'Graph\n' + '\n'.join([
    str(line) for line in graph
    ]) + f"Size {len(graph)}x{len(graph[0])}"
legend_text += '\n\nCordinates\n' + '\n'.join([
    str(line) for line in coordinates
    ]) + f"Size {len(coordinates)}x{len(coordinates[0])}\n\n"

res = dict()
# key - time, value - edges
for line in enumerate(graph):
    for item in enumerate(line[1]):
        if item[1]:
            x_1, x_2 = x[line[0]], x[item[0]]
            y_1, y_2 = y[line[0]], y[item[0]]
            plt.plot([x_1, x_2],[y_1, y_2], color='Black')
            
            # angle = (np.arctan((y_2 - y_1)/(x_2 - x_1))*180)/np.pi 
            speed = graph[line[0]][item[0]]
            distance = round(np.sqrt((y_2 - y_1) ** 2 + (x_2 - x_1) ** 2), 2)
            time = round(distance/speed, 4)
            data_to_annotate = f'd={distance} v={speed} t={time} \n'
            if (f'V{line[0]}+V{item[0]}:     ' + data_to_annotate)  not in legend_text:
                legend_text += f'V{line[0]}+V{item[0]}:     ' + data_to_annotate
                if time in res.keys():
                    res[time].append([f'V{line[0]}+V{item[0]}', distance])
                else:
                    res[time] = [f'V{line[0]}+V{item[0]}', distance]
            # ax.annotate(str(data_to_annotate),  xy=(x_2 - (x_2 - x_1)/2, y_2 - (y_2 - y_1)/2), rotation=angle) # try to print data under connection
            print([x[line[0]], x[item[0]]],[y[line[0]], y[item[0]]])
else:
    legend_text += '\n'
time = min(res.keys())
    

if len(res[time]) < 2:
    # if more then 1 distance with the same time
    legend_text += f'min distance {res[time][1]} between {res[time][0]}\n'
else:
    # I hope that will work XD 
    legend_text += f'min distance {res[time][1]} between {res[time][0]}\n'
    for item in res[time][2:]:
        legend_text += f'min distance {item[1]} between {item[0]}'
plt.axis('off')
plt.plot(-10, -10, label=legend_text)
plt.legend(loc="upper left")
plt.show()

