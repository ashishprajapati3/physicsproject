import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Streamlit App
st.title("Differential Equation Solver")

# User Input
st.sidebar.header("Equation Parameters")
equation = st.sidebar.text_input("Enter the equation in Python syntax (e.g., 'y - x')", "y - x")
x0 = st.sidebar.number_input("Initial x (x0)", value=0.0)
y0 = st.sidebar.number_input("Initial y (y0)", value=1.0)
x_max = st.sidebar.number_input("Max x", value=10.0)
steps = st.sidebar.slider("Number of steps", min_value=10, max_value=1000, value=100)

# Function to evaluate the differential equation
def func(x, y):
    return eval(equation, {"x": x, "y": y, "np": np})

# Solve ODE
x_vals = np.linspace(x0, x_max, steps)
solution = solve_ivp(func, [x0, x_max], [y0], t_eval=x_vals)

# Plot solution
st.subheader("Solution")
fig, ax = plt.subplots()
ax.plot(solution.t, solution.y[0], label=f"Solution of dy/dx = {equation}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# Display solution values
st.subheader("Solution Data")
st.write("x values:", solution.t)
st.write("y values:", solution.y[0])