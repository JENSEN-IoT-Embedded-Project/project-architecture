
```mermaid
graph TD
    subgraph Edge["Edge Layer (IoT with Soft RTS)"]
        subgraph Devices["Physical Devices"]
            A[Ultrasonic Sensor from Kit]
            B["Pico W<br/>(Python, C, C++)"]
        end
        
        subgraph Processing["Edge Processing"]
            C["Local Processing:<br/>- Data Serialization<br/>- Device ID Addition<br/>- Initial Aggregation"]
        end
    end

    subgraph Cloud["Cloud Infrastructure"]
        E["MQTT Broker:<br/>- Docker on Fly.io<br/>- Advanced Processing<br/>- Soft RTS Management"]
        F["InfluxDB (TSDB):<br/>- Line Protocol<br/>- Cloud Aggregation<br/>- Time Series Data"]
        G["RESTful API:<br/>- Data Access Layer<br/>- Service Integration"]
    end

    subgraph Interface["User Interface Layer"]
        H["GUI:<br/>- Mobile App<br/>- Web Interface<br/>- Real-time Updates"]
        I["Twilio Service:<br/>- SMS Gateway<br/>- Alert Management"]
        J["End User"]
    end

    A -->|"Sensor Data"| B
    B -->|"Processed Data<br/>+ Device ID<br/>Wi-Fi / 4G<br/>ARP, DNS, TCP, MQTT"| C
    C -->|"Processed Data<br/>+ Device ID"| E
    E -->|"Line Protocol<br/>Time Series Data"| F
    E -->|"RESTful API<br/>JSON Format"| G
    F -->|"Aggregated Data"| G
    G -->|"Cloud Communication<br/>Secure WebSocket"| H
    G -->|"Notification Trigger"| I
    I -->|"SMS Alert"| J

    classDef edge fill:#f9f33333,stroke:#333,stroke-width:2px
    classDef cloud fill:#9f988888,stroke:#3336,stroke-width:2px
    classDef api fill:#f994,stroke:#3337,stroke-width:2px
    classDef ui fill:#fb34,stroke:#3338,stroke-width:2px
    classDef sms fill:#6cf5,stroke:#3339,stroke-width:2px

    class A,B,C edge
    class E,F cloud
    class G api
    class H ui
    class I,J sms


