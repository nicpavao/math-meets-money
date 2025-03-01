use std::collections::HashMap;

struct VibesEngine {
    transport_modes: HashMap<&'static str, f64>,
}

impl VibesEngine {
    fn new() -> Self {
        let mut transport_modes = HashMap::new();
        transport_modes.insert("Cargo Ship Isolation", 10.0);
        transport_modes.insert("Private Jet Glam", 9.5);
        transport_modes.insert("Cross-Country Train Musings", 8.5);
        transport_modes.insert("Driving Solo in a Prius", 4.0);
        transport_modes.insert("Public Bus at Rush Hour", 1.0);
        transport_modes.insert("Walking in NYC", 6.5);
        transport_modes.insert("Biking in Amsterdam", 7.8);
        Self { transport_modes }
    }

    fn rate(&self, mode: &str) -> f64 {
        *self.transport_modes.get(mode).unwrap_or(&0.0)
    }

    fn best_vibes(&self) {
        let (best, score) = self.transport_modes.iter().max_by(|a, b| a.1.partial_cmp(b.1).unwrap()).unwrap();
        println!("🚢 Best vibes award goes to: {} with a score of {:.1}!", best, score);
    }
}

fn main() {
    let engine = VibesEngine::new();
    engine.best_vibes();
    println!("Private Jet Glam vibes: {:.1}", engine.rate("Private Jet Glam"));
    println!("Walking in NYC vibes: {:.1}", engine.rate("Walking in NYC"));
    println!("Taking a subway at 2 AM vibes: {:.1}", engine.rate("Subway at 2 AM"));
}