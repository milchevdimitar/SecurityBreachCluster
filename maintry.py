from interface import HttpsSecurityInterface
from normalization import normalize_readable_request, normalize_unreadable_request

def main():
    interface = HttpsSecurityInterface()
    raw_readable_request = {
        'method': 'POST',
        'url_length': 350,
        'header_count': 15,
        'body_length': 2000,
        'has_cookie': True,
        'user_agent_length': 100,
        'url': 'https://example.com/api/login',
        'query_string': 'user=admin',
        'content_type': 'application/json'
    }

    features_readable = normalize_readable_request(raw_readable_request)
    label_readable = 0

    score_r = interface.analyze_readable(features_readable, label_readable)
    print(f"Readable HTTPS request prediction score: {score_r:.3f}")

    raw_unreadable_request = {
        'packet_size': 1300,
        'encrypted': True,
        'tls_version': 1.3,
        'cipher_suite': 4865,
        'flags': 0b101,
        'time_since_last_packet_ms': 50
    }

    features_unreadable = normalize_unreadable_request(raw_unreadable_request)
    label_unreadable = 1
    score_u = interface.analyze_unreadable(features_unreadable, label_unreadable)
    print(f"Unreadable HTTPS request prediction score: {score_u:.3f}")

if __name__ == "__main__":
    main()
