
# Unit-1 Traffic Engineering And Signaling

<!-- 1. Telecommunication Traffic:
    - unit of Traffic , Traffic measurement.
    - A mathematical model:
        1. Lost call systems:
            - Theory , Traffic Performance.
            - Loss systems in tandem.
            - Traffic tables.
        2. Queueing systems: 
            - Erlang Distribution
            -Probability of delay
2. Signaling:
    - CCITT Signaling System and Digital Customers line Signaling -->

----------------------------------

## Telephone Traffic profile:

1. operater thus offer cheaper call rates during off-peak hours. It costs them almost nothing to carry such calls

2. if they manage to shift some calls from peak and thus capital expenditure are needed.

[call-hours-vs-time]()

## Traffic:
1. the traffic intensity (Sometimes refered as simply as Traffic) is defined as the average number of calls in progress simultaneously during a particular period of time.

2.  traffic intensity is a measure of the average occupancy of a server or resource during a specified period of time, normally a busy hour. It is measured in traffic units (erlangs) and defined as the ratio of the time during which a facility is cumulatively occupied to the time this facility is available for occupancy.

## Erlang:

1. It is dimensionless but name is given by Erlang(unit).
2. One Erlang (E) represents the amount of traffic carried by a trunk that is completely occupied i.e one call-hour per hour or one minute per minute.

3. Traffic carried by a group of trunks is :

## Formula:
<center>
    <h1>
$Traffic$ = $A$  = $\frac {C \times h}{T}$
    </h1>
</center>

- **where**:    
    - A = Traffic in Erlang 
    - C = Average number of call arrivals during time T
    - h = average call holding time 

    - 1 erlang = 36 ccs (centum call second per hour)

