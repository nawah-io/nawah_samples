import { Component, OnInit } from '@angular/core';
import { Doc, NawahService, Res } from 'ng-nawah';

@Component({
	selector: 'app-admin-comment-pending-list',
	templateUrl: './admin-comment-pending-list.component.html',
	styleUrls: ['./admin-comment-pending-list.component.css']
})
export class AdminCommentPendingListComponent implements OnInit {

	comments: Array<Doc> = [];

	constructor(private nawah: NawahService) { }

	ngOnInit() {
		this.readComments();
	}

	readComments(): void {
		this.nawah.call({
			endpoint: 'blog_comment/read',
			query: [{ status: 'pending' }],
			awaitAuth: true
		}).subscribe({
			next: (res) => {
				this.comments = res.args.docs;
			},
			error: (err: Res<Doc>) => {
				alert(`Unexpected error occurred: ${err.msg || err}`);
			}
		});
	}

	approveComment(_id: string): void {
		if (confirm('Are you sure you want to approve this comment?')) {
			let note: string = prompt('Status note?', '');
			this.nawah.call({
				endpoint: 'blog_comment/update',
				query: [{
					_id: _id
				}],
				doc: {
					status: 'approved',
					status_note: note,
				}
			}).subscribe({
				next: (res) => {
					this.readComments();
				},
				error: (err: Res<Doc>) => {
					alert(`Unexpected error occurred: ${err.msg || err}`);
				}
			});
		}
	}

	deleteComment(_id: string): void {
		if (confirm('Are you sure you want to delete this comment?')) {
			let note: string = prompt('Status note?', '');
			this.nawah.call({
				endpoint: 'blog_comment/update',
				query: [{
					_id: _id
				}],
				doc: {
					status: 'deleted',
					status_note: note,
				}
			}).subscribe({
				next: (res) => {
					this.readComments();
				},
				error: (err: Res<Doc>) => {
					alert(`Unexpected error occurred: ${err.msg || err}`);
				}
			});
		}
	}

}
