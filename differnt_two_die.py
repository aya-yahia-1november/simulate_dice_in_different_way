from die import Die
import  pygal
die1=Die()
die2=Die(10)
results=[]
for roll_num in range(50000):
    result=die1.roll()+die2.roll()
    results.append(result)
print(results)

# analyze the results
frequencies=[]
max_value =die1.num_sides+die2.num_sides
for value in range(2,max_value+1):
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist=pygal.Bar()
hist.title="Resulting of rolling D6 and D10 50000 times"
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title="Resulting"
hist.y_title='Frequency of result'
hist.add("D6+D10",frequencies)
hist.render_to_file("two_different_die_visual.svg")