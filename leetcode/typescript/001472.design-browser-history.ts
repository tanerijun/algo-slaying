class Visit {
	public readonly val: string;
	public prev?: Visit;
	public next?: Visit;

	constructor(site: string) {
		this.val = site;
	}
}

class BrowserHistory {
	private cur: Visit;

	constructor(homepage: string) {
		this.cur = new Visit(homepage);
	}

	visit(url: string): void {
		this.cur.next = new Visit(url);
		this.cur.next.prev = this.cur;
		this.cur = this.cur.next;
	}

	back(steps: number): string {
		for (let i = 0; i < steps; i++) {
			if (this.cur.prev) {
				this.cur = this.cur.prev;
			} else {
				break;
			}
		}

		return this.cur.val;
	}

	forward(steps: number): string {
		for (let i = 0; i < steps; i++) {
			if (this.cur.next) {
				this.cur = this.cur.next;
			} else {
				break;
			}
		}

		return this.cur.val;
	}
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
