import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import itertools

def graph_BloxPot(graphTitle, data, randomDists, xLabel, yLabel):
    fig, ax1 = plt.subplots(figsize=(10, 6))
    fig.canvas.set_window_title(graphTitle)
    plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

    bp = plt.boxplot(data, notch=0, sym='+', vert=1, whis=1.5)
    plt.setp(bp['boxes'], color='black')
    plt.setp(bp['whiskers'], color='black')
    plt.setp(bp['fliers'], color='red', marker='+')

    # Add a horizontal grid to the plot, but make it very light in color
    # so we can use it for reading data values but not be distracting
    ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                   alpha=0.5)

    # Hide these grid behind plot objects
    ax1.set_axisbelow(True)
    #ax1.set_title('Comparison of IID Bootstrap Resampling Across Five Distributions')
    ax1.set_xlabel(xLabel)
    ax1.set_ylabel(yLabel)

    # Now fill the boxes with desired colors
    boxColors = ['royalblue'] #'darkkhaki', 
    numBoxes = 5
    medians = list(range(numBoxes))
    #boxCoords = [[]]
    for i in range(numBoxes):
        box = bp['boxes'][i]
        boxX = []
        boxY = []
        for j in range(5):
            boxX.append(box.get_xdata()[j])
            boxY.append(box.get_ydata()[j])
        boxCoords = list(zip(boxX, boxY))
        # Alternate between Dark Khaki and Royal Blue
        
        #k = i % 2
        #facecolor=boxColors[k]
        
        #boxPolygon = Polygon(boxCoords[i], facecolor='royalblue')
        boxPolygon = Polygon(boxCoords, facecolor='royalblue')
        ax1.add_patch(boxPolygon)
        # Now draw the median lines back over what we just filled in
        med = bp['medians'][i]
        medianX = []
        medianY = []
        for j in range(2):
            medianX.append(med.get_xdata()[j])
            medianY.append(med.get_ydata()[j])
            plt.plot(medianX, medianY, 'k')
            medians[i] = medianY[0]
        # Finally, overplot the sample averages, with horizontal alignment
        # in the center of each box
        plt.plot([np.average(med.get_xdata())], [np.average(data[i])],
                 color='w', marker='*', markeredgecolor='k')

    # Set the axes ranges and axes labels
    #ax1.set_xlim(0.5, numBoxes + 0.5)
    ax1.set_xlim(0.4, numBoxes + 0.4)
    top = max(list(itertools.chain.from_iterable(data)))
    bottom = min(list(itertools.chain.from_iterable(data)))
    ax1.set_ylim(bottom, top)
    xtickNames = plt.setp(ax1, xticklabels=randomDists)
    plt.setp(xtickNames, rotation=45, fontsize=8)

    # Due to the Y-axis scale being different across samples, it can be
    # hard to compare differences in medians across the samples. Add upper
    # X-axis tick labels with the sample medians to aid in comparison
    # (just use two decimal places of precision)
    pos = np.arange(numBoxes) + 1
    upperLabels = [str(np.round(s, 2)) for s in medians]
    weights = ['bold', 'semibold']
    for tick, label in zip(range(numBoxes), ax1.get_xticklabels()):
        k = tick % 2
        ax1.text(pos[tick], top + (top * 0.01), upperLabels[tick],
                 horizontalalignment='center', size='small', weight=weights[k],
                 color='black')

    # Finally, add a basic legend
    #plt.figtext(0.80, 0.08, str(500) + ' Random Numbers',
                #backgroundcolor=boxColors[0], color='black', weight='roman',
                #size='x-small')
    #plt.figtext(0.80, 0.045, 'IID Bootstrap Resample',
                #backgroundcolor=boxColors[0],
                #color='white', weight='roman', size='x-small')
    #plt.figtext(0.80, 0.015, '*', color='white', backgroundcolor='silver',
                #weight='roman', size='medium')
    #plt.figtext(0.815, 0.013, ' Average Value', color='black', weight='roman',
                #size='x-small')

    plt.show()

if __name__ == '__main__':
    #Independent Variables
    randomDists = ['ACM', 'IEEE*', 'IEEE', 'Scidirect','Springer']
    xLabel = 'Search Engine'

    metamorphic_relations = ['MPTitle', 'MPublished', 'MPShuffleJD', 'Top1Absent']

    if (len(sys.argv) == 1):
        print('Usage: python bloxplot.py relation (\'MPTitle\', \'MPublished\', \'MPShuffleJD\', \'Top1Absent\')')
        sys.exit(-1)

    metamorphic_relation = str(sys.argv[1]) #Metamorphic Relation

    if (metamorphic_relation == 'MPTitle'):
        #MPTitle
        yLabel = 'ROCOA every 30 runs' #Rate of Occurrence of Anomaly

        ACM  = [0, 0, 0, 0, 0, 0.0666666666666667, 0.0333333333333333, 0, 0, 0, 0, 0, 0, 0, 0.0666666666666667, 0, 0, 0, 0.0666666666666667, 0, 0, 0.0333333333333333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        IEEE_old  = [0.133333333333333, 0.2, 0.0666666666666667, 0.0666666666666667, 0.133333333333333, 0.1, 0.166666666666667, 0.166666666666667, 0.0666666666666667, 0.166666666666667, 0.2, 0.133333333333333, 0.1, 0.133333333333333, 0.133333333333333, 0.0666666666666667, 0.133333333333333, 0.0666666666666667, 0.333333333333333, 0.1, 0.0666666666666667, 0.0666666666666667, 0.133333333333333, 0.0333333333333333, 0.2, 0.233333333333333, 0.133333333333333, 0.1, 0.133333333333333, 0.166666666666667, 0.1, 0.133333333333333, 0.0333333333333333]
        IEEE  = [0.033333333, 0.033333333, 0.066666667, 0.033333333, 0, 0, 0, 0.033333333, 0, 0.033333333, 0.1, 0.133333333, 0, 0.033333333, 0.1, 0.033333333, 0.166666667, 0.066666667, 0.1, 0.033333333, 0, 0.033333333, 0.066666667, 0.066666667, 0, 0.033333333, 0.066666667, 0.066666667, 0, 0.066666667, 0.033333333, 0.033333333, 0.133333333]
        SciDirect = [0.0333333333333333, 0.0333333333333333, 0.0666666666666667, 0.0333333333333333, 0, 0, 0, 0.0333333333333333, 0, 0.0333333333333333, 0.1, 0.133333333333333, 0, 0.0333333333333333, 0.1, 0.0333333333333333, 0.166666666666667, 0.0666666666666667, 0.1, 0.0333333333333333, 0, 0.0333333333333333, 0.0666666666666667, 0.0666666666666667, 0, 0.0333333333333333, 0.0666666666666667, 0.0666666666666667, 0, 0.0666666666666667, 0.0333333333333333, 0.0333333333333333, 0.133333333333333]
        Springer = [0, 0.1, 0.0666666666666667, 0.0666666666666667, 0, 0.0333333333333333, 0, 0.0333333333333333, 0, 0, 0, 0, 0, 0, 0, 0, 0.0666666666666667, 0, 0.0333333333333333, 0, 0, 0.1, 0, 0, 0.1, 0.0333333333333333, 0, 0, 0, 0, 0.1, 0, 0]
        
    elif (metamorphic_relation == 'MPublished'):
        #MPublished
        yLabel = 'ROCOF every 30 runs' #Rate of Occurrence of Failure

        ACM  = [0.233333333333333, 0.333333333333333, 0.366666666666667, 0.333333333333333, 0.233333333333333, 0.333333333333333, 0.266666666666667, 0.333333333333333, 0.233333333333333, 0.266666666666667, 0.2, 0.333333333333333, 0.2, 0.266666666666667, 0.4, 0.3, 0.366666666666667, 0.266666666666667, 0.366666666666667, 0.233333333333333, 0.266666666666667, 0.4, 0.4, 0.466666666666667, 0.366666666666667, 0.3, 0.366666666666667, 0.133333333333333, 0.233333333333333, 0.1, 0.266666666666667, 0.233333333333333, 0.4]
        IEEE_old  = [0.133333333333333, 0.266666666666667, 0.2, 0.1, 0.166666666666667, 0.166666666666667, 0.1, 0.2, 0.2, 0.1, 0.1, 0.233333333333333, 0.266666666666667, 0.2, 0.2, 0.1, 0.2, 0.2, 0.233333333333333, 0.0333333333333333, 0.233333333333333, 0.166666666666667, 0.0333333333333333, 0.266666666666667, 0.233333333333333, 0.166666666666667, 0.3, 0.2, 0.1, 0.0666666666666667, 0.166666666666667, 0.133333333333333, 0.166666666666667]
        IEEE  = [0.533333333, 0.466666667, 0.4, 0.4, 0.366666667, 0.4, 0.366666667, 0.466666667, 0.3, 0.533333333, 0.466666667, 0.3, 0.366666667, 0.366666667, 0.233333333, 0.3, 0.466666667, 0.533333333, 0.5, 0.4, 0.2, 0.4, 0.3, 0.566666667, 0.266666667, 0.4, 0.366666667, 0.466666667, 0.4, 0.533333333, 0.4, 0.333333333, 0.333333333]
        SciDirect = [0, 0, 0, 0, 0, 0, 0, 0, 0.0333333333333333, 0, 0, 0.0333333333333333, 0, 0, 0, 0.0333333333333333, 0, 0, 0, 0, 0, 0.0333333333333333, 0, 0.0333333333333333, 0.0333333333333333, 0, 0, 0, 0, 0.0333333333333333, 0.0333333333333333, 0, 0]
        Springer = [0.1, 0.0666666666666667, 0.133333333333333, 0.1, 0.1, 0.1, 0.0666666666666667, 0.0333333333333333, 0.133333333333333, 0.0666666666666667, 0.1, 0.0666666666666667, 0.133333333333333, 0.133333333333333, 0.1, 0.0666666666666667, 0.0666666666666667, 0.1, 0.133333333333333, 0.1, 0.1, 0.0666666666666667, 0.2, 0.2, 0.1, 0.2, 0.1, 0.2, 0.0666666666666667, 0.0666666666666667, 0.1, 0.1, 0.0666666666666667]

    elif (metamorphic_relation == 'MPShuffleJD'):
        #MPShuffleJD
        yLabel = 'Jaccard Similarity Coefficient'

        ACM  = [0.365, 0.398333333333333, 0.225, 0.341666666666667, 0.462592592592593, 0.336666666666667, 0.343333333333333, 0.186666666666667, 0.275, 0.266666666666667, 0.25, 0.231666666666667, 0.306666666666667, 0.34, 0.313333333333333, 0.303333333333333, 0.401666666666667, 0.406666666666667, 0.166666666666667, 0.326666666666667, 0.248333333333333, 0.261666666666667, 0.243333333333333, 0.23, 0.308333333333333, 0.208333333333333, 0.285, 0.241111111111111, 0.32, 0.346666666666667, 0.243333333333333, 0.330606060606061, 0.303333333333333]
        IEEE_old  = [0.309333333333333, 0.421333333333333, 0.518666666666667, 0.358666666666667, 0.328, 0.430666666666667, 0.393333333333333, 0.325333333333333, 0.442666666666667, 0.425333333333333, 0.505333333333333, 0.438666666666667, 0.484, 0.389333333333333, 0.432, 0.398666666666667, 0.505333333333333, 0.352, 0.54, 0.445333333333333, 0.444, 0.461333333333333, 0.424, 0.473333333333333, 0.705333333333333, 0.44, 0.389333333333333, 0.293333333333333, 0.302666666666667, 0.310666666666667, 0.328, 0.498666666666667, 0.312]
        IEEE = [0.488, 0.370666667, 0.36, 0.210666667, 0.232, 0.38, 0.398666667, 0.3, 0.293333333, 0.338666667, 0.338666667, 0.3, 0.238666667, 0.316, 0.2, 0.390666667, 0.38, 0.461333333, 0.437333333, 0.270666667, 0.412, 0.438666667, 0.270666667, 0.416, 0.322666667, 0.350666667, 0.362666667, 0.418666667, 0.361333333, 0.546666667, 0.698666667, 0.225333333, 0.470666667]
        SciDirect = [0.338666666666667, 0.306666666666667, 0.385333333333333, 0.269333333333333, 0.318761904761905, 0.221333333333333, 0.2, 0.322666666666667, 0.170666666666667, 0.372, 0.298111365369947, 0.348, 0.253333333333333, 0.361333333333333, 0.346666666666667, 0.342666666666667, 0.402666666666667, 0.344, 0.330666666666667, 0.538666666666667, 0.333333333333333, 0.264, 0.273333333333333, 0.410666666666667, 0.433333333333333, 0.225894736842105, 0.336, 0.206666666666667, 0.182666666666667, 0.385101449275362, 0.396592592592592, 0.365333333333333, 0.238333333333333]
        Springer = [0.96921052631579, 0.987602339181287, 1, 0.993333333333333, 0.874187995240627, 0.984444444444444, 0.962745098039216, 0.996666666666667, 0.961904761904762, 0.992592592592593, 0.971520467836257, 1, 0.921666666666667, 0.93, 0.996666666666667, 1, 0.989454191033138, 0.957777777777778, 0.966666666666667, 0.972962962962963, 0.95280701754386, 0.921666666666667, 1, 0.980392156862745, 0.994736842105263, 1, 0.93, 0.946410256410256, 0.982962962962963, 0.987037037037037, 0.936246781540899, 0.964814814814815, 0.98]

    elif (metamorphic_relation == 'Top1Absent'):
        #Top1Absent
        yLabel = 'ROCOA every 30 runs' #Rate of Occurrence of Anomaly

        ACM  = [0.0333333333333333, 0,0000, 0,0000, 0.0333333333333333, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000, 0,0000]
        IEEE_old  = [0.1, 0.0666666666666667, 0.1, 0.166666666666667, 0.1, 0.233333333333333, 0.0333333333333333, 0.133333333333333, 0.2, 0.266666666666667, 0.0666666666666667, 0.166666666666667, 0.2, 0.133333333333333, 0.166666666666667, 0.2, 0.166666666666667, 0.166666666666667, 0.0666666666666667, 0.0333333333333333, 0.166666666666667, 0.133333333333333, 0.1, 0.233333333333333, 0.3, 0.3, 0.0666666666666667, 0.2, 0.133333333333333, 0.2, 0.133333333333333, 0.233333333333333, 0.166666666666667]
        IEEE  = [0.933333333, 0.8, 0.866666667, 0.766666667, 0.766666667, 0.766666667, 0.7, 0.833333333, 0.833333333, 0.766666667, 0.933333333, 0.833333333, 0.8, 0.833333333, 0.8, 0.9, 0.9, 0.666666667, 0.9, 0.9, 0.733333333, 0.933333333, 0.833333333, 0.866666667, 0.9, 0.9, 0.8, 0.866666667, 0.733333333, 0.733333333, 0.7, 0.866666667, 0.833333333]
        SciDirect = [0.1333, 0.1000, 0.0667, 0.0667, 0.0000, 0.0333, 0.0333, 0.0667, 0.0333, 0.0667, 0.0333, 0.1000, 0.1333, 0.1667, 0.0000, 0.0000, 0.0667, 0.0667, 0.0000, 0.0667, 0.0333, 0.1000, 0.0000, 0.0667, 0.1667, 0.0333, 0.1000, 0.0000, 0.1000, 0.0667, 0.1000, 0.0667, 0.0000]
        Springer = [0.1000, 0.0333, 0.0000, 0.0333, 0.0000, 0.0000, 0.0333, 0.0000, 0.0000, 0.0000, 0.0000, 0.0333, 0.0000, 0.0333, 0.0000, 0.0000, 0.1000, 0.0000, 0.0000, 0.0667, 0.0000, 0.0333, 0.0667, 0.0333, 0.0000, 0.0667, 0.0000, 0.0333, 0.1000, 0.0000, 0.0000, 0.0000, 0.0000]

    data = [ACM, IEEE_old, IEEE, SciDirect, Springer]   
    graph_BloxPot(metamorphic_relation, data, randomDists, xLabel, yLabel)    