import pandas as pd
import matplotlib.pyplot as plt

data = {'Emotion': ['Happy', 'Sad', 'Angry'], 'Count': [50, 30, 20]}
df = pd.DataFrame(data)

df.plot(kind='bar', x='Emotion', y='Count', color='skyblue')
plt.title("Emotion Distribution")
plt.show()
