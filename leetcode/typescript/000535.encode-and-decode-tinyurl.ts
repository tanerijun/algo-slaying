const encodedMap = new Map<string, string>();

/**
 * Encodes a URL to a shortened URL.
 */
function encode(longUrl: string): string {
  const shortUrl = (encodedMap.size + 1).toString();
  encodedMap.set(shortUrl, longUrl);
  return shortUrl;
}

/**
 * Decodes a shortened URL to its original URL.
 */
function decode(shortUrl: string): string {
  const longUrl = encodedMap.get(shortUrl);
  if (!longUrl) {
    throw new Error(`${shortUrl} doesn't exist in database`);
  }
  return longUrl;
}

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */

// Time complexity: O(1) for both encoding and decoding
// Space complexity: O(1)
// Scalability is also really great even using only number as the encoded URL.
// To scale even higher, we can also include alphabets.
