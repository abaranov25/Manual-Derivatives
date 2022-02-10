# Manual-Derivatives
An independent project of computationally calculating derivatives for discontinuous functions (Work in progress)

Project Description:
The idea of this project is that calculating derivatives mathematically fails when functions are discontinuous. Therefore,
it is impossible to approximate a discontinuous function with a Taylor series. This project seeks to computationally
take the nth derivative of a function given a finite set of points that lie on the graph, and then use a Taylor series to
approximate the function that best represents the input points.


The approximate function has been made with the two following tasks in mind:


Interpolation:    The output function will predict values between provided input points with great accuracy. This has use in tracking
                  historical data such as speed in between measurements.
      
Extrapolation:    The output function can extend to further points, but accuracy diminishes as the range of the function increases.
                  However, extrapolations can be made and are sometimes accurate. One example is Covid-19 case numbers
                  over the course of the pandemic.


Progress: 
The approximate function has been made and works well with mathematically definable functions (such as f(x) = x * cos(2x)). However,
it has yet to be seen how the function performs under real world data.
