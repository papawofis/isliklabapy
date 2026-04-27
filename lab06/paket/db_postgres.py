import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="particles_db",
        user="postgres",
        password="12345"
    )

def save_result(particle, specific, compton):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id SERIAL PRIMARY KEY,
            particle TEXT,
            specific TEXT,
            compton TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        )
    """)
    
    cur.execute(
        "INSERT INTO results (particle, specific, compton) VALUES (%s, %s, %s)",
        (particle, specific, compton)
    )
    
    conn.commit()
    cur.close()
    conn.close()

def get_all_results():
    """Получает все результаты из БД"""
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT id, particle, specific, compton FROM results ORDER BY id DESC")
    rows = cur.fetchall()
    
    results = []
    for row in rows:
        results.append({
            'id': row[0],
            'particle': row[1],
            'specific': row[2],
            'compton': row[3]
        })
    
    cur.close()
    conn.close()
    return results
